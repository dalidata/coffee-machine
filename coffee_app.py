import streamlit as st
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialisation des objets
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Titre de l'application
st.title("☕ Machine à Café Interactive")
st.markdown("---")

# État de la machine (géré avec Streamlit)
if "is_on" not in st.session_state:
    st.session_state.is_on = True

if "message" not in st.session_state:
    st.session_state.message = ""

# Fonction pour afficher les rapports
def afficher_rapport():
    with st.expander("📊 Rapport de la machine", expanded=True):
        st.subheader("Ressources disponibles :")
        resources = coffee_maker.report()
        for key, value in resources.items():
            st.write(f"{key}: {value}")
        
        st.subheader("Profit :")
        st.write(f"{money_machine.profit} {money_machine.CURRENCY}")



# Interface principale
if st.session_state.is_on:
    st.header("Options disponibles :")
    options = menu.get_items().strip("/").split("/")
    choice = st.selectbox("Sélectionnez votre boisson :", options + ["Rapport", "Éteindre"])

   

    if choice == "Rapport":
        afficher_rapport()

    else:
        drink = menu.find_drink(choice)
        if drink:
            st.write(f"**Prix : {drink.cost} {money_machine.CURRENCY}**")
            montant = st.number_input("💰 Insérez le montant :", min_value=0.0, step=0.5, format="%.2f")

            if st.button("Payer"):
                if montant >= drink.cost:
                    if coffee_maker.is_resource_sufficient(drink):
                        coffee_maker.make_coffee(drink)
                        change = round(montant - drink.cost, 2)
                        money_machine.profit += drink.cost
                        st.success(f"✅ Votre {choice} est prêt ! Rendu de monnaie : {change} {money_machine.CURRENCY}")
                    else:
                        st.error("❌ Ressources insuffisantes pour préparer cette boisson.")
                else:
                    st.error("❌ Fonds insuffisants. Veuillez insérer plus d'argent.")
        else:
            st.warning("🔴 La machine est éteinte. Merci et à bientôt !")
