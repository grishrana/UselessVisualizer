import streamlit as st


def about_page():
    st.title("About Us")
    st.write(
        """
    We believe that the most unexpected ideas often lead to the most innovative solutions. Our theme revolves around embracing the unusual, the strange, and the seemingly absurd—because if it works, who’s to say it’s not brilliant?
    """
    )

    st.subheader("What We Do")
    st.write(
        """
    We create unique and challenging applications that push the boundaries of conventional thinking. Our projects are designed to make you think, laugh, and maybe even scratch your head in confusion—until you realize that it’s all part of the fun!
    """
    )

    st.subheader("Our Vision")
    st.write(
        """
    Our mission is to challenge conventional thinking by developing projects that make you pause and reconsider what’s possible. We aim to entertain, provoke thought, and most importantly, inspire you to think outside the box.
    """
    )

    st.subheader("Our Team")
    # Split the team members into columns
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/grish_rana.jpg", width=280)
        st.write("### Grish Rana")
        st.markdown(
            "[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/grishrana)"
        )
        st.markdown(
            "[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/grishrana)"
        )

        st.write("**Currently Studying:** Software Engineering at Pokhara University")
        st.write(
            "**Bio:** Enthusiastic about data science and Python, with a focus on turning data into actionable insights."
        )

    with col2:
        st.image("images/damodar_bagale.jpg", width=280)
        st.write("### Damodar Bagale")
        st.markdown(
            "[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/damodarbagaleofficial)"
        )
        st.markdown(
            "[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/Sushil346)"
        )
        st.write("**Currently Studying:** Computer Engineering at Tribhuvan University")
        st.write(
            "**Bio:** Has a strong interest in AI/ML development. Enjoys hiking and exploring new tech gadgets in his free time."
        )

    st.subheader("Our Philosophy")
    st.write(
        """
    "Embrace the unconventional; innovation often hides where logic fears to tread. By exploring the absurd, we unlock doors to new possibilities and perspectives."
    """
    )

    st.subheader("Inspirational Quotes")

    st.write(
        """
    “It’s not about ideas. It’s about making ideas happen.” – Scott Belsky             
     Innovation thrives not just on creativity, but on the action that brings ideas to life.
    
             
    “The best way to predict the future is to invent it.” – Alan Kay             
     The path to innovation is paved with bold ideas and the courage to bring them into reality.
    """
    )


# Call the function to render the page
about_page()
