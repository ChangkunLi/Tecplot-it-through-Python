clear;

global r0 alpha beta d0 theta0 delta_theta delta_phi
r0 = 1.55;
alpha = 0.49;
beta = -0.10;
d0 = 0.64;
theta0 = 1;
delta_theta = 0.29;
delta_phi = 0.48;

N_theta = 51;
theta = linspace(0,pi/2,N_theta);
N_phi = 50;
phi = linspace(-pi,pi,N_phi+1);
phi = phi(1:N_phi);

N = 1 + (N_theta - 1)*N_phi;
A = ones(N,4);
for i = 2:N_theta
    for j = 1:N_phi
        r = r0*(2/(1+cos(theta(i))))^(alpha + beta*(cos(phi(j)))^2) - r_ind(theta(i),phi(j));
        A((i-2)*N_phi+j,1) = r*cos(theta(i));
        A((i-2)*N_phi+j,2) = r*sin(theta(i))*cos(phi(j));
        A((i-2)*N_phi+j,3) = r*sin(theta(i))*sin(phi(j)) + 0.2;
    end
end
A(N,1) = r0;
A(N,2) = 0;
A(N,3) = 0.2;

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

! rm -f Zhong.dat
! touch Zhong.dat

f = fopen('Zhong.dat','r+');
fprintf(f,'TITLE="3D_Zhong_Surface"\n');
fprintf(f,'VARIABLES ="X [R]", "Y [R]", "Z [R]", "Rho [amu/cm^3]"\n');
fprintf(f,'ZONE T="Zhong", N=    %d, E=   %d, F=FEPOINT, ET=QUADRILATERAL\n',N,E);
fprintf(f,'%f\t%f\t%f\t%f\n',A');
fprintf(f,'%4d\t%4d\t%4d\t%4d\n',C');
fclose(f);

function f = r_ind(theta,phi)
    global d0 theta0 delta_theta delta_phi
    f = d0*exp(-((theta-theta0)/delta_theta)^2/2)*(exp(-((phi-pi/2)/delta_phi)^2/2) + exp(-((phi+pi/2)/delta_phi)^2/2));
end

