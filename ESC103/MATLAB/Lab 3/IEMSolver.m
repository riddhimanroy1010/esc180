function [x, y, t] = IEMSolver(e, f, g, h, x_0, y_0, T, N)
    A = [e f; g h];
    dt = T/N;
    t = 0:dt:T;
    
    SOL = NaN(2, length(t));
    SOL(1, 1) = x_0;
    SOL(2, 1) = y_0;

    for k = 2:length(t)
        SOL(:,k) = SOL(:,k-1) + dt*A*SOL(:,k-1);
        SOL(:,k) = SOL(:,k - 1) + (A*dt/2)*(SOL(:,k - 1) + SOL(:,k));
    end

    x = SOL(1, :);
    y = SOL(2, :);
end