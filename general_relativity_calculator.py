from einsteinpy.symbolic.riemann import RiemannCurvatureTensor, ChristoffelSymbols
from einsteinpy.symbolic import MetricTensor
from einsteinpy.symbolic.ricci import RicciTensor, RicciScalar
import sympy

# See link for instructions
# https://hub.gke2.mybinder.org/user/einsteinpy-einsteinpy-758fivng/notebooks/docs/source/examples/Playing%20with%20Contravariant%20and%20Covariant%20Indices%20in%20Tensors(Symbolic).ipynb

sympy.init_printing()

M, l = sympy.symbols('M l') # symbolically define mass and AdS radius or any other symbol you have in your metric that is not a coordinate

tau, r, phi = sympy.symbols("tau r phi") # symbolically define the coordinates

# write the components of the metric for convenience
g_tau_tau = l**2*(r**2-8*M)
g_r_r = l**2*(r**2-8*M)**(-1)
g_phi_phi = l**2*r**2

m = sympy.diag(g_tau_tau, g_r_r, g_phi_phi).tolist() # diagonal metric into a list
metric = MetricTensor(m, syms = (tau, r, phi)) # make the list into a MetricTensor object

chr = ChristoffelSymbols.from_metric(metric) # calculate the christoffel symbols
print(chr.config) # returns for example ull meaning the first index is up and the second and third index are down
print(chr) # prints a list of lists containing all the components 
print(chr[0, 1, 2]) # prints the \Gamma^\tau_r_\phi component notice how the symbols were given in the metric in the order tau, r, phi that is why 0 corresponds to tau etc

rm = RiemannCurvatureTensor.from_christoffels(chr) # calculate Riemann tensor
print(rm.config)
print(rm)

rt = RicciTensor.from_riemann(rm) # calculate Ricci tensor
print(rt.config)
print(rt)

rs = RicciScalar.from_riccitensor(rt) # calculate Ricci scalar
print(rs)

print(chr[1, 1, 1]) # Since symbols were given in as tau r phi, r corresponds to 1, tau to 0 and phi to 2 so this is Gamma^r_rr

