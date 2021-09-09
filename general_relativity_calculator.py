from einsteinpy.symbolic.riemann import RiemannCurvatureTensor, ChristoffelSymbols
from einsteinpy.symbolic import MetricTensor
from einsteinpy.symbolic.ricci import RicciTensor, RicciScalar
import sympy

# See link for instructions
# https://hub.gke2.mybinder.org/user/einsteinpy-einsteinpy-758fivng/notebooks/docs/source/examples/Playing%20with%20Contravariant%20and%20Covariant%20Indices%20in%20Tensors(Symbolic).ipynb

sympy.init_printing()

M, l = sympy.symbols('M l')

tau, r, phi = sympy.symbols("tau r phi")

g_tau_tau = l**2*(r**2-8*M)
g_r_r = l**2*(r**2-8*M)**(-1)
g_phi_phi = l**2*r**2

m = sympy.diag(g_tau_tau, g_r_r, g_phi_phi).tolist()
metric = MetricTensor(m, syms = (tau, r, phi))

chr = ChristoffelSymbols.from_metric(metric)
print(chr.config)
print(chr)

rm = RiemannCurvatureTensor.from_christoffels(chr)
print(rm.config)
print(rm)

rt = RicciTensor.from_riemann(rm)
print(rt.config)
print(rt)

rs = RicciScalar.from_riccitensor(rt)
print(rs)

print(chr[1, 1, 1]) # Since symbols were given in as tau r phi, r corresponds to 1, tau to 0 and phi to 2 so this is Gamma^r_rr

