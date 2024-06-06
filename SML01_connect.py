from RsInstrument import *
#import RsInstrument as rsi

instr = RsInstrument('ASRL4::INSTR', id_query=True, reset=False)
idn = instr.query_str('*IDN?')
print('Hello, I am: ' + idn)

#fréquence d'utilisation du générateur
freq = instr.query_str('FREQuency?')
print("Fréquence d'utilisation: " + freq)

instr.write_str('FREQ 82MHz')

instr.write_str('POW -1.6dBm')

#Set RF output ON/OFF

instr.write_str('OUTP:STAT ON')

# Close the session
instr.close()
