%Problem 1
clear
clc
w = [2.9, 2.1, 2.3, 2.1, 1.8, 2.7, 1.5, 2.9, 1.5];
d = [2.4, 1.5, 2.4, 1.8, 1.8, 2.9, 1.2, 3, 1.2];
x = w;
y = d;
A = [ones(length(x), 1), x', x'.^2];
b = y';

x_ls = (A' * A) \ (A' * b);
x_vec = linspace(1, 3);

lin_fit = (x_ls(3) * x_vec.^2) + (x_ls(2) * x_vec) + (x_ls(1));
scatter(x, y, "o");
hold on;
plot(x_vec, lin_fit, "--");
hold off

%problem 2
clear
clc

N = [5, 10, 15, 20, 100];
y_0 = 1;
t_0 = 0;
figure
title("IEM Approx");
xlabel("t");
ylabel("y");
hold on
for n = N
    delta_t = 2/n;
    t = 0:delta_t:2;
    sol = NaN(1, length(t));
    sol(1) = y_0;
    for k = 2 : length(t)
        sol(k) = sol(k - 1) + delta_t*(((t(k - 1))^2) - 2*(sol(k - 1)));
        sol(k) = sol(k - 1) + (delta_t/2)*(((t(k - 1) + t(k))^2) - 2*(sol(k - 1) + sol(k)));
    end
    plot(t, sol)
    
end
legend("N = 5", "N = 10", "N = 15", "N = 20", "N = 100", "location", "southeast");

hold off;