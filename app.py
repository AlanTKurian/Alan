# import dash
# import dash_html_components as html
# import dash_core_components as dcc
# from dash.dependencies import Input, Output

# app = dash.Dash(__name__)

# app.layout = html.Div(
#     [
#         html.H1("About Me"),
#         html.Div(
#             [
#                 html.Img(src='assets/alan.jpg', className="profile-photo"),
#                 html.Div(
#                     [
#                         html.H2("Alan Thomas"),
#                         html.H3("Data Scientist"),
#                         html.P("Dynamic data professional adept at understanding and modeling data to create impactful solutions and drive business value. Proven track record in developing machine learning models, MLOps pipelines, and DevOps pipelines, as well as excelling in Dash front-end development, BI, and reporting. Skilled in managing stakeholders and leading projects in the FMCG Industry (Supply Domain). Passionate about exploring challenges in Econometrics, Macro-Economics, Economics of Climate Change, and Health Economics. Seeking opportunities to contribute to business growth while pursuing personal development")
#                     ],
#                     className="profile-details"
#                 ),
#             ],
#             className="about-me-section",
#         ),
#         html.H2("Skills"),
#         html.Div(
#             [
#                 html.P("Python, R, SQL, Machine Learning, Data Visualization"),
#                 # Add more skills here
#             ],
#             className="skills-section",
#         ),
#         html.H2("Education and Certifications"),
#         html.Div(
#             [
#                 html.P("Masters in Economics, Madras School of Economics"),
#                 html.P("Bachelor of Science in Economics, Mathematics, Statistics, CHRIST (Deemed to be University)"),
#                 # Add more education and certifications here
#             ],
#             className="education-section",
#         ),
#         html.H2("Experience"),
#         html.Div(
#             [
#                 html.P("Data Scientist, Anheuser-Busch InBev (2021- Present)"),
                
#                 # Add more experience details here
#             ],
#             className="experience-section",
#         ),
#         html.H2("Projects / Blogs "),
#         html.Div(
#             [
#                 html.Div(
#                     [
#                         html.H3("Blog 1"),
#                         html.P("Designing an MLops Pipeline Using MLFLOW Tracking & Azure Databricks Workflow — Part 1"),
#                         html.A("Medium", href="https://medium.com/@alanthomasnk/designing-an-mlops-pipeline-using-azure-databricks-workflow-along-with-mlflow-tracking-ab8bab8fc09f", target="_blank"),
#                     ],
#                     className="project-item",
#                 ),
#                 # html.Div(
#                 #     [
#                 #         html.H3("Project 2"),
#                 #         html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac felis id est faucibus pharetra eu a mauris. Nullam a lorem odio. Donec ac ligula vel elit tincidunt fermentum. Phasellus rutrum varius magna, a iaculis elit ullamcorper nec. Integer varius suscipit odio, sed posuere nisl hendrerit a."),
#                 #         html.A("GitHub Repository", href="link_to_project2_repository", target="_blank"),
#                 #     ],
#                 #     className="project-item",
#                 # ),
#                 # Add more project items here
#             ],
#             className="projects-section",
#         ),
#         html.H2("Publications/ Term Papers"),
#         html.Div(
#             [
#                 html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac felis id est faucibus pharetra eu a mauris. Nullam a lorem odio. Donec ac ligula vel elit tincidunt fermentum. Phasellus rutrum varius magna, a iaculis elit ullamcorper nec."),
#                 # Add more publications here
#             ],
#             className="publications-section",
#         ),
#         html.H2("Contact"),
#         html.Div(
#             [
#                 html.P("Email: alanthomasnk@gmail.com"),
#                 html.A("LinkedIn", href="https://www.linkedin.com/in/alanthomasnk/", target="_blank"),
#                 html.Br(),
#                 html.A("GitHub", href="https://github.com/AlanTKurian", target="_blank"),
#             ],
#             className="contact-section",
#         ),
#         html.H2("Testimonials"),
#         html.Div(
#             [
#                 html.Img(src='assets/Capture.PNG', className="profile-photo"),
#                 # html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac felis id est faucibus pharetra eu a mauris. Nullam a lorem odio. Donec ac ligula vel elit tincidunt fermentum. Phasellus rutrum varius magna, a iaculis elit ullamcorper nec."),
#                 # Add more testimonials here
#             ],
#             className="testimonials-section",
#         ),
#     ],
#     className="main-container",
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)

import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("About Me"),
        html.Div(
            [
                html.Img(src='assets/alan.jpg', className="profile-photo"),
                html.Div(
                    [
                        html.H2("Alan Thomas"),
                        html.H3("Data Scientist"),
                        html.P("Dynamic data professional adept at understanding and modeling data to create impactful solutions and drive business value. Proven track record in developing machine learning models, MLOps pipelines, and DevOps pipelines, as well as excelling in Dash front-end development, BI, and reporting. Skilled in managing stakeholders and leading projects in the FMCG Industry (Supply Domain). Passionate about exploring challenges in Econometrics, Macro-Economics, Economics of Climate Change, and Health Economics. Seeking opportunities to contribute to business growth while pursuing personal development")
                    ],
                    className="profile-details"
                ),
            ],
            className="about-me-section",
        ),
        html.H2("Skills"),
        html.Div(
            [
                html.P("Python, R, SQL, Machine Learning, Data Visualization"),
                # Add more skills here
            ],
            className="skills-section",
        ),
        # Rest of your code...

        html.H2("HTML File"),
        html.Iframe(srcDoc=open("htmlfile.html", "r").read(), className="html-file-iframe")
    ],
    className="main-container",
)

if __name__ == "__main__":
    app.run_server(debug=True)
