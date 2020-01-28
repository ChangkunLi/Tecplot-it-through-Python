clear;

r0 = 1.55;
alpha = 0.4;

N_theta = 51;
theta = linspace(0,pi/2,N_theta);
N_phi = 50;
phi = linspace(-pi,pi,N_phi+1);
phi = phi(1:N_phi);

N = 1 + (N_theta - 1)*N_phi;
A = ones(N,6);
for i = 2:N_theta
    normal_0 = [(alpha*sin(theta(i))*sin(theta(i)) + cos(theta(i))*(1 + cos(theta(i))))/...
        (-alpha*sin(theta(i))*cos(theta(i)) + sin(theta(i))*(1 + cos(theta(i)))), 1, 0];
    normal_0 = normal_0/norm(normal_0);
    
    for j = 1:N_phi
        r = r0*(2/(1+cos(theta(i))))^alpha;
        A((i-2)*N_phi+j,1) = r*cos(theta(i));
        A((i-2)*N_phi+j,2) = r*sin(theta(i))*cos(phi(j));
        A((i-2)*N_phi+j,3) = r*sin(theta(i))*sin(phi(j)) + 0.2;
        A((i-2)*N_phi+j,4) = normal_0(1);
        A((i-2)*N_phi+j,5) = normal_0(2)*cos(phi(j));
        A((i-2)*N_phi+j,6) = normal_0(2)*sin(phi(j));
    end
end
A(N,1) = r0;
A(N,2) = 0;
A(N,3) = 0.2;
A(N,4) = 1;
A(N,5) = 0;
A(N,6) = 0;

E = N_phi*(N_theta - 1);
C = zeros(E,4);
for i = 1:N_theta-1    
    for j = 1:N_phi
        C((i-1)*N_phi+j,1) = (i-1)*N_phi + j;
        C((i-1)*N_phi+j,2) = (i-1)*N_phi + mod(j,N_phi) + 1;
        if i ==1
            C((i-1)*N_phi+j,3) = N;
            C((i-1)*N_phi+j,4) = N;
        else
            C((i-1)*N_phi+j,3) = (i-2)*N_phi + mod(j,N_phi) + 1;
            C((i-1)*N_phi+j,4) = (i-2)*N_phi + j;
        end
    end
end

! rm -f Shue.dat
! touch Shue.dat

f = fopen('Shue.dat','r+');
fprintf(f,'TITLE="3D_Shue_Surface"\n');
fprintf(f,'VARIABLES ="X [R]", "Y [R]", "Z [R]", "MP_Nx", "MP_Ny", "MP_Nz"\n');
fprintf(f,'ZONE T="Shue", N=    %d, E=   %d, F=FEPOINT, ET=QUADRILATERAL\n',N,E);
fprintf(f,'%f\t%f\t%f\t%f\t%f\t%f\n',A');
fprintf(f,'%4d\t%4d\t%4d\t%4d\n',C');
fclose(f);
