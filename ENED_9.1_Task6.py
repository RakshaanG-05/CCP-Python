temp = float(input("Enter temperature (°C): "))
sn_input = float(input("Enter percentage of tin (just the number or decimal): "))

if sn_input <= 1:
    sn = sn_input * 100
else:
    sn = sn_input

if sn <= 61.9:
    l_temp = -2.326 * sn + 327
else:
    l_temp = 1.286 * (sn - 61.9) + 183

if temp >= l_temp:
    lead_phase = "Molten"
    tin_phase = "Molten"
elif temp < 183:
    lead_phase = "Solid"
    tin_phase = "Solid"
else:
    if sn <= 61.9:
        lead_phase = "Solid"
        tin_phase = "Molten"
    else:
        lead_phase = "Molten"
        tin_phase = "Solid"

print("Lead Phase:", lead_phase)
print("Tin Phase:", tin_phase)