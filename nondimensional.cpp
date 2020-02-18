#include "iostream"
#include "fstream"
#include "sstream"
#include "string"
#include "vector"
#include "cmath"
#include <Eigen/Dense>

using namespace::std;
using namespace::Eigen;

#define nT2T 1.0/1000000000.0
#define non2T 2*2440000.0*sqrt(3.14159265359*1.6726)/100000000000000.0
#define Rm 2440000.0
#define D(a,b,xyz) (Data(Connectivity(Nele,a) - 1,xyz) - Data(Connectivity(Nele,b) - 1,xyz))*(Data(Connectivity(Nele,a) - 1,xyz) - Data(Connectivity(Nele,b) - 1,xyz))

struct cut_sphere
{
public:
    // Definition of constructor
    
    cut_sphere() = default;
    cut_sphere(const string &s){
        ifstream file;
        file.open(s);
        string line;
        string str1 = ", N=";
        string str2 = ", E=";
        string str3 = ", F=";
        int pos1;
        int pos2;
        int pos3;
        int N,E;
        for(int i = 0;i<23;i++){
            getline(file,line);
            if(i==1){
                int found1, found2;
                found2 = -1;
                found1 = line.find("\"",found2+1);
                while(found1!=string::npos){
                    found2 = line.find("\"",found1+1);
                    Pars.push_back(line.substr(found1+1,found2-found1-1));
                    found1 = line.find("\"",found2+1);
                }
            }
            if(i==2){
                pos1 = line.find(str1);
                pos2 = line.find(str2);
                pos3 = line.find(str3);
                string Nstr = line.substr(pos1+str1.size(),pos2-pos1-str1.size());
                string Estr = line.substr(pos2+str2.size(),pos3-pos2-str2.size());
                istringstream strm(Nstr);
                strm >> N;
                strm.clear();
                strm.str(Estr);
                strm >> E;
                Data = MatrixXd::Ones(N,Pars.size());
                Connectivity = MatrixXi::Ones(E,4);
            }
        }
        istringstream strm;
        for(int i = 0;i<N;i++){
            getline(file,line);
            strm.str(line);
            for(int j = 0;j<Pars.size();j++){
                strm >> Data(i,j);
            }
            strm.clear();
        }
        for(int i = 0;i<E;i++){
            getline(file,line);
            strm.str(line);
            for(int j = 0;j<4;j++){
                strm >> Connectivity(i,j);
            }
            strm.clear();
        }
        file.close();
    }

    double open_flux(){
        int index[7];
        double flux = 0;
        for(int i = 0; i < Pars.size();i++){
            if(Pars[i] == "X"){
               index[0] = i;
            }
            if(Pars[i] == "Y"){
               index[1] = i;
            }
            if(Pars[i] == "Z"){
               index[2] = i;
            }
            if(Pars[i] == "B_x"){
               index[3] = i;
            }
            if(Pars[i] == "B_y"){
               index[4] = i;
            }
            if(Pars[i] == "B_z"){
               index[5] = i;
            }
            if(Pars[i] == "Status"){
               index[6] = i;
            }
        }
        for(int i = 0; i<Connectivity.rows(); i++){
            flux += cell_flux(i,index);
        }
        return flux;
    }

private:
    double cell_flux(int Nele, int* param){
        int count = 0;
        double fraction = 0.0;    
        for(int i = 0;i<4;i++){
            if(Data(Connectivity(Nele,i) - 1,param[6]) <= 2.5 && Data(Connectivity(Nele,i) - 1,param[6]) >= 2.0){
                count += 1;
            }
        }
        if(count != 0){
            fraction = count/4.0;
            MatrixXd bar_param = MatrixXd::Zero(6,1);
            for(int i = 0;i<4;i++){
                for(int j = 0;j<5;j++){
                    bar_param(j,0) += Data(Connectivity(Nele,i) - 1,param[j])/4.0;
                }
            }   
            double radius = sqrt(bar_param(0,0)*bar_param(0,0) + bar_param(1,0)*bar_param(1,0) + bar_param(2,0)*bar_param(2,0));
            double Bn = 0.0;
            for(int i = 0;i<3;i++){
                Bn += bar_param(i,0)*bar_param(i+3,0)/radius;        
            }
            // if(fraction<1){
            //     cout << "Boundary cell found" << endl;
            // }
            double S = area(Nele);
            // return fraction*Bn*S*nT2T*Rm*Rm;
            return fraction*Bn*S*non2T*Rm*Rm;
        }
        else{
            return 0.0;
        }
    }

public:
    // dimensionless area
    double area(int Nele){
        // First triangle
        double s1;
        double a,b,c;

        a = sqrt(D(0,1,0) + D(0,1,1) + D(0,1,2));
        b = sqrt(D(0,2,0) + D(0,2,1) + D(0,2,2));
        c = sqrt(D(2,1,0) + D(2,1,1) + D(2,1,2));

        s1 = sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))/4.0;
        // Second triangle
        double s2;

        a = sqrt(D(0,3,0) + D(0,3,1) + D(0,3,2));
        b = sqrt(D(0,2,0) + D(0,2,1) + D(0,2,2));
        c = sqrt(D(2,3,0) + D(2,3,1) + D(2,3,2));

        s2 = sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))/4.0;      

        return s1+s2;  
    }

    // Definition of data

    MatrixXd Data;
    MatrixXi Connectivity;
    vector<string> Pars;
};

int main()
{
    system("ls cut*.dat > file.txt");
    ifstream in1;
    in1.open("file.txt");
    string line;
    vector<string> filename;
    while(getline(in1,line)){
        filename.push_back(line);
    }
    in1.close();
    int N_file = filename.size();

    for(int i = 0; i<N_file; i++){
        cut_sphere test(filename[i]);
        cout << test.open_flux() << endl;
    }

    return 0;
}
