'''
This file and the contents have been taken from the
Churnometer walk through Project 2 and customized for
this project
'''
import streamlit as st


def page_project_hypothesis_body():

    st.info(
        f"### Project Hypothesis and Validation\n\n"
        f"* I have found 4 hypothesis and their validation:\n\n"
        f"1. Hypothesis one.\n"
        f"* We consider the price of houses to be higher if the house has had "
        f"larger surface measured in sq. ft. \n"
        f"* A correlation study can help in investigating if this is true.\n\n"
        f"2. Hypothesis Two.\n"
        f"* We consider that the houses with the same util surface measured "
        f"in sq. ft. but built more recently has had a higher price then a "
        f"older built home. \n"
        f"* A correlation study can help in investigating if this is true.\n\n"
        f"3. Hypothesis Three.\n"
        f"* We consider the houses with the same util surface measured in sq. ft "
        f"built in a recent year but remodeled recently has had a higher price "
        f"then a house built in the same year but not recently modeled.\n"
        f"* A correlation study can help in investigating if this is true.\n\n"
        f"4. Hypothesis Four.\n"
        f"* We consider that a house with simila sq. ft., but with a higher "
        f"quality of materials and condition scores might have had a "
        f"higher sale price./n"
        f"* A correlation study can help in investigating if this is true."
    )