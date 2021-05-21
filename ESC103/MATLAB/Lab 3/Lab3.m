clear;
clc;
% Setting Up Constants
e = 0;
f = -1;
g = 1;
h = 0;
x0 = 1;
y0 = 0;
T = 10;

%grid creation for true sol
step = 0.01;
t_real = 0:step:T;
x_real = cos(t_real);
y_real = sin(t_real);

%EM plotting
figure
subplot(2, 1, 1);
plot(t_real, x_real);
hold on
xlabel("time");
ylabel("x(t)");
title("EM Solving");

subplot(2, 1, 2);
plot(t_real, y_real);
hold on
xlabel("time");
ylabel("y(t)");
title("EM Solving");
%EM Solving
 for N = [10, 50, 100, 200]
     subplot(2, 1, 1)
     [x_est, y_est, t_est] = EMSolver(e, f, g, h, x0, y0, T, N);
     plot(t_est, x_est);
     
     subplot(2, 1, 2)
     plot(t_est, y_est);
     
 end 
 legend("Actual function", "N = 10", "N = 50", "N = 100", "N = 200");
 hold off;
 
%IEM Plotting
figure
subplot(2, 1, 1);
plot(t_real, x_real);
hold on
xlabel("time");
ylabel("x(t)");
title("IEM Solving");

subplot(2, 1, 2);
plot(t_real, y_real);
hold on
xlabel("time");
ylabel("y(t)");
title("IEM Solving");
%EM Solving
 for N = [10, 50, 100, 200]
     subplot(2, 1, 1)
     [x_est, y_est, t_est] = IEMSolver(e, f, g, h, x0, y0, T, N);
     plot(t_est, x_est);
     
     subplot(2, 1, 2)
     plot(t_est, y_est);
     
 end 
 legend("Actual function", "N = 10", "N = 50", "N = 100", "N = 200");
 hold off;
 

 