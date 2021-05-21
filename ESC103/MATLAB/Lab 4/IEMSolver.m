function [x, y, t] = IEMSolver(A, x_0, y_0, xd_1, xd_2, T, N)
    dt = T/N;
    t = 0:dt:T;
    
    SOL = NaN(4, length(t));
    SOL(1, 1) = x_0;
    SOL(2, 1) = y_0;
    SOL(3, 1) = xd_1;
    SOL(4, 1) = xd_2;

    for k = 2:length(t)
        SOL(:,k) = SOL(:,k-1) + dt*A*SOL(:,k-1);
        SOL(:,k) = SOL(:,k - 1) + (A*dt/2)*(SOL(:,k - 1) + SOL(:,k));
    end

    x = SOL(1, :);
    y = SOL(2, :);
end
