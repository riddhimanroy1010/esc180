clear;
M = zeros(2, 4);
M(1, :) = [20 30 40 50];
M(2, :) = [8 23 28 34];
humid = M(1, :);
elec = M(2, :);
x = (M(1, :) - 35) / 5;

A = zeros(4, length(x));
A(1, :) = x.^3;
A(2, :) = x.^2;
A(3, :) = x; 
A(4, :) = A(4, :) + 1;
A = A';

y = elec';
%u = [A b]';
A_star = A' * A;
u_star = A' * y;

u = mldivide(A_star, u_star);
u = u';

x_vec = linspace(-3, 3, 100);
cubic_fit = u(1).*x_vec.^3 + u(2).*x_vec.^2 + u(3).*x_vec + u(4);
scatter(x, y);
hold on;
plot(x_vec, cubic_fit);
xlabel("Coded Humidity");
ylabel("Conductivity");
legend("Plotted data", "Cubic Best Fit");
title("Cubic Fit for Coded Humidity vs Electrical Condictivity");