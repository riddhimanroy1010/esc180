clear;
humidity_percent = [20, 30, 40, 50];
elec_cond = [8, 23, 28, 34];
x = (humidity_percent - 35)./ 5;
%linear fit
lin_fit_x = polyfit(x, elec_cond, 1);
lin_fit = polyval(lin_fit_x, x);
%quadratic fit
quad_fit_x = polyfit(x, elec_cond, 2);
quad_fit = polyval(quad_fit_x, x);
%cubic fit
cube_fit_x = polyfit(x, elec_cond, 3);
cube_fit = polyval(cube_fit_x, x);
%plotting
scatter(x, elec_cond, "o");
hold on;
plot(x, lin_fit, "b");
plot(x, quad_fit, "k");
plot(x, cube_fit, "r");
