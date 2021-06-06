function [X_norm, mu, sigma] = featureNormalize(X)

X_norm = X;
mu = zeros(1, size(X, 2));
sigma = zeros(1, size(X, 2));

for i=1:size(X, 2),
    mu(1, i) = mean(X(:, i))
    sigma(1, i) = std(X(:, i))
end

X_norm = (X .- mu) ./ sigma

end
