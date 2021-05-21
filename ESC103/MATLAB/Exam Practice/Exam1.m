clear
clc
t = [10, 15, 20, 25, 40, 50, 55, 60, 75];
ten_strength = [5, 20, 18, 40, 33, 54, 70, 60, 78];
x = t;
y = ten_strength;
A = [ones(length(x), 1), x'];
b = y';

x_ls = (A' * b) \ (A' * A);
x_vec = linspace(0, 80);

lin_fit = (x_ls(2) * x_vec) + x_ls(1);
scatter(x, y, "o");
hold on;
plot(x_vec, lin_fit);