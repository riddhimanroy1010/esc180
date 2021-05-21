clear;
clc;
k1 = 4.66;
k2 = 4.66;
m1 = 0.0917;
m2 = 0.0765;

A = [
    0, 1, 0, 0;
    -(k1+k2)/m1, 0, k2/m1, 0;
    0, 0, 0, 1;
    k2/m2, 0, -k2/m2, 0;
];

t = 100;
N = 10000;

Xinit = [
    100,
    0,
    50,
    0
];

solution = IEMsolver(A,Xinit,t,N);
x1 = solution(1, :);
x2 = solution(3, :);


yfft = abs(fft(x2));
t_list = linspace(0,t,N+1);

plot(t_list,x1)
xlim([0 10])

function SOL = IEMsolver(A,i,T,N)
    dt = T/N;
    t = 0:dt:T;
    SOL = NaN(length(i), length(t));
    SOL(:,1) = i;

    for(k = 2:length(t))
        % k1 = A*SOL(k-1)
        % k2 = A*SOL(:,k)
        old_euler = SOL(:,k-1) + dt*A*SOL(:,k-1);

        SOL(:,k) = SOL(:,k-1) + 0.5*dt*(A*SOL(:, k-1) + A*old_euler);
    end
end