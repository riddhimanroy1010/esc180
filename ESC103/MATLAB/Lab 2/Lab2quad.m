clear;
M = zeros(2, 4);
M(1, :) = [20 30 40 50];
M(2, :) = [8 23 28 34];
humid = M(1, :);
elec = M(2, :);
x = (M(1, :) - 35) / 5;

A = zeros(3, length(x));
A(1, :) = x.^2;
A(2, :) = x;
A(3, :) =  A(3, :) + 1;
A = A';

y = elec';
%u = [A b]';
A_star = A' * A;
u_star = A' * y;

u = mldivide(A_star, u_star);
u = u';

x_vec = linspace(-3, 3, 100);
quad_fit = u(1).*x_vec.^2 + u(2).*x_vec + u(3);
scatter(x, y);
hold on;
plot(x_vec, quad_fit);
xlabel("Coded Humidity");
ylabel("Conductivity");
legend("Plotted data", "Quadratic Best Fit");
title("Quadratic Fit for Coded Humidity vs Electrical Condictivity");
