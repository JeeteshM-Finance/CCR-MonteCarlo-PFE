#**Monte Carlo CCR Engine**

**Overview**

This project simulates future interest rate scenarios for an Interest Rate Swap using Monte Carlo Simulation and computes CCR Exposure Metrics like EE and PFE. 

**Features**
1. Monte Carlo Simulation of Interest Rate paths
2. IRS MTM Calculation
3. Positive Exposure Calculation
4. Expected Exposure (EE)
5. 95 %ile PFE
6. Exposure Profile Visualization

**Brief workflow**

1. Generating Interest Rate Paths
2. Revalue Interest Rate Swap
3. Calculate MTM
4. Calculate Postive Exposure
5. Compute EE and PFE
6. Visualize Exposures

**Sample Output**

==================================================
COUNTERPARTY CREDIT RISK SIMULATION
==================================================

TRADE DETAILS
--------------------------------------------------
Traded Product: Interest Rate Swap
Notional Amount: $100,000,000
Maturity: 5
Fixed Leg Rate: 5.00 %

SIMULATION DETAILS
--------------------------------------------------
Monte Carlo Simulations: 100000
Time Steps: 60

EXPOSURE RESULTS
--------------------------------------------------
Peak Expected Exposure: $1.73 Million
95th %ile PFE: $7.11 Million

==================================================
SIMULATION COMPLETED SUCCESSFULLY
==================================================


<img width="676" height="394" alt="image" src="https://github.com/user-attachments/assets/b8cf67bf-04d4-4e89-88e7-ceb85d67d10f" />







**Future Improvements**

1. Evolving interest rate model like Hull White
2. Inclusing Collateral and Netting
3. Including multiple derivative products
4. Extension to calculate further metrics of an entire portfolio
5. Streamlit for a real time interactive dashboard 
