clc;
clear;
%Setting up constants
k1 = 4.66;
k2 = k1;
m1 = 0.0917;
m2 = 0.0765;
x1_i = 100;
x2_i = 50;
x1_sd_i = (((-1*k1*x1_i) - k2*(x1_i - x2_i))/m1);
x2_sd_i = (-k2/m2)*(x2_i - x1_i);
x1_fd_i = 0;
x2_fd_i = 0;
time = 10;

%coefficient matrix, does differentiation
A = zeros(4, 4);
A(1, 3) = 1;
A(2, 4) = 1;
A(3, 1) = A(1, 1) + -2*k1/m1;
A(3, 2) = A(1, 2)+ k2/m1;
A(4, 1) = A(2, 1) + k2/m2;
A(4, 2) = A(2, 2) + -1*k2/m2;


%Solving IVP
dt = [1/50, 1/100, 1/200, 1/500, 1/1000];
figure
subplot(2, 1, 1);
xlabel("time");
ylabel("x1(t)");
title("IEM Solving")
hold on

subplot(2, 1, 2);
xlabel("time");
ylabel("x2(t)");
title("IEM Solving")
hold on

for delta_t = dt
    [x1_est, x2_est, time_est] = IEMSolver(A, x1_i, x2_i, x1_fd_i, x2_fd_i, time, 10/delta_t);
    subplot(2, 1, 1)
    plot(time_est, x1_est)

    subplot(2, 1, 2)
    plot(time_est, x2_est)
end
subplot(2, 1, 1)
legend("N = 1/50", "N = 1/100", "N = 1/200", "N = 1/500", "location", "eastoutside")
subplot(2, 1, 2)
legend("N = 1/50", "N = 1/100", "N = 1/200", "N = 1/500", "location", "eastoutside")
hold off

%delta_t = 1000 is good enough, identical behavior to higher fidelity ones.

figure

subplot(2, 1, 1);
title("x2 - x1");
xlabel("time");
plot(time_est, x2_est - x1_est, "k")

subplot(2, 1, 2);
plot(time_est, x1_est + x2_est, "r")
title("x1 + x2");
xlabel("time")
%Resonant 1: 11.72hz, from plot 1
%Resonant 2: 4.67hz, from plot 2

eigens = eig(A)
%eigen frequencies
%Resonant 1: 11.85hz
%Resonant 2: 4.69hz






