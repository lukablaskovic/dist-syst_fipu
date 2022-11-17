"""
Servis 2
Drugi servis se sastoji od jedne rute. (/parseActivities)
Unutar drugog servisa aktivnosti se filtriraju ovisno o type, te se zatim
prosljeđuju trećem servisu. Charity i Recreational se šalju na posebnu
rutu trećeg servisa (/charityAndRecreational), ostale se šalju na običnu
rutu (/otherActivities).
"""