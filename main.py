import numpy as np
import matplotlib.pyplot as plt

#Model Parameters
traded_product = "Interest Rate Swap"
initial_rate = 0.05     # 5%
volatility = 0.01       # 1%
years = 5
steps = 60              #Monthly steps
simulations = 100000

dt = years / steps

plt.figure(figsize=(10,6))

#Derivative Product information
notional = 100_000_000          #100Mn
fixed_rate = 0.05               #5%

#Storing all simulations for Exposure Metrics usage
all_exposures = []

#Simulating paths
for sim in range (simulations):

    interest_rates = [initial_rate]
    swap_values = []
    exposures = []
    for step in range(steps):
        shock = np.random.normal(0,1)
        new_rate = interest_rates[-1] + volatility * np.sqrt(dt) * shock

        interest_rates.append(new_rate)
        remaining_time = years - (step + 1) * dt

        mtm = (notional * (new_rate - fixed_rate) * remaining_time)
    
        swap_values.append(mtm)
        exposure = max(mtm, 0)
        exposures.append(exposure)
    all_exposures.append(exposures)

all_exposures = np.array(all_exposures)
EE = np.mean(all_exposures, axis = 0)

PFE = np.percentile(all_exposures, 95, axis = 0)

#Output
print("="*50)
print("COUNTERPARTY CREDIT RISK SIMULATION")
print("="*50)

print()

print("TRADE DETAILS")
print("-"*50)
print(f"Traded Product: {traded_product}")
print(f"Notional Amount: ${notional:,.0f}")
print(f"Maturity: {years}")
print(f"Fixed Leg Rate: {fixed_rate*100:.2f} %")

print()

print("SIMULATION DETAILS")
print("-"*50)
print(f"Monte Carlo Simulations: {simulations}")
print(f"Time Steps: {steps}")

print()

print("EXPOSURE RESULTS")
print("-"*50)
print(f"Peak Expected Exposure: ${max(EE)/1e6:.2f} Million")
print(f"95th %ile PFE: ${max(PFE)/1e6:.2f} Million")

print()

print("="*50)
print("SIMULATION COMPLETED SUCCESSFULLY")
print("="*50)

plt.plot(EE/1e6, linewidth = 3, label = "Expected Exposure")
plt.plot(PFE/1e6, linewidth = 3, label = "95% PFE")

plt.title(f"CCR Exposure Profile for {traded_product}")
plt.xlabel("Time (Years)")
plt.ylabel("Exposure ($ Million)")
plt.grid(True)
plt.legend()
plt.savefig(f"CCR Exposure Profile - {traded_product}.png", dpi = 300)