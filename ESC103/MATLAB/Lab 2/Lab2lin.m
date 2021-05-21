clear;
M = zeros(2, 4);
M(1, :) = [20 30 40 50];
M(2, :) = [8 23 28 34];
humid = M(1, :);
elec = M(2, :);
x = (M(1, :) - 35) / 5;

A = zeros(2, length(x));
A(1, :) =  A(1, :) + 1;
A(2, :) = x;
A = A';

y = M(2, :)';
%u = [A b]';
A_star = A' * A;
u_star = A' * y;

u = mldivide(A_star, u_star);
u = u';

lin_fit = u(1).*x + u(2);
scatter(x, y);
hold on;
plot(x, lin_fit);
xlabel("Coded Humidity");
ylabel("Conductivity");
legend("Plotted data", "Linear Best Fit");
title("Linear Fit for Coded Humidity vs Electrical Condictivity");