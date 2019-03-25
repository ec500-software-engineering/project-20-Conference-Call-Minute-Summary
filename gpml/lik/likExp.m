function [varargout] = likExp(link, hyp, varargin)
% LIKEXP Exponential likelihood function for strictly positive data y.
%
% Report number of hyperparameters
%  s = LIKEXP ()
%  s = LIKEXP (link)
%
% Prediction mode
%   lp            = LIKEXP (link, hyp, y, mu)
%  [lp, ymu, ys2] = LIKEXP (link, hyp, y, mu, s2)
%
% Inference mode
%  [varargout] = LIKEXP (link, hyp, y, mu, s2, inf)
%  [varargout] = LIKEXP (link, hyp, y, mu, s2, inf, i)
%
% Call likFunctions to get an explanation of outputs in each mode.
%
% The expression for the likelihood is
%
%  likExp(f) = exp(-y/mu) / mu
%
% with mean = mu and variance = mu^2 where mu = g(f) is the intensity, f is a
% Gaussian process, y is the strictly positive data. Hence, we have
%
%   llik(f) = log(likExp(f)) = -y / g(f) - log(g(f)).
%
% Internally, the function is in fact a wrapper around likGamma with hyper
% parameter al = 1.
%
% There are no hyperparameters:
%
% hyp = [ ]
%
% We provide two inverse link functions 'exp' and 'logistic':
%
%   g(f) = exp(f) and g(f) = log(1+exp(f))).
%
% The link functions are located at util/glm_invlink_*.m.
% Note that for the 'exp' intensity the likelihood lik(f) is log concave.
%
% Several modes are provided, for computing likelihoods, derivatives and moments
% respectively, see likFunctions.m for the details. In general, care is taken
% to avoid numerical issues when the arguments are extreme.
%
% See also LIKFUNCTIONS, LIKGAMMA

% Copyright (c) by Hannes Nickisch, 2013-10-29.

if nargin<4, varargout = {'0'}; return; end   % report number of hyperparameters
varargout = cell(nargout, 1);    % allocate the right number of output arguments
for j=1:nargout, varargout{j} = []; end                      % derivative output
if nargin<=6, [varargout{:}] = likGamma(link,0,varargin{:}); end   % log(al) = 0
