from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# Sample data for Data Structures & Algorithms (DSA) resources
ds_papers = [
    {'title': 'DSA Paper 2021', 'link': 'https://www.scribd.com/document/411053815/Data-Structure-Question-Paper-with-Answer-pdf'},
    {'title': 'DSA Paper 2020', 'link': 'https://example.com/ds-papers/2020'},
    {'title': 'DSA Paper 2019', 'link': 'https://example.com/ds-papers/2019'},
]

ds_practice_questions = [
    {'title': 'DSA Practice Set 1', 'link': 'https://example.com/ds-practice/1'},
    {'title': 'DSA Practice Set 2', 'link': 'https://example.com/ds-practice/2'},
    {'title': 'DSA Practice Set 3', 'link': 'https://example.com/ds-practice/3'},
]

ds_textbooks = [
    {'title': 'Introduction to Algorithms', 'link': 'https://example.com/textbooks/intro-to-algorithms'},
    {'title': 'Data Structures and Algorithm Analysis in Java', 'link': 'https://example.com/textbooks/dsa-analysis-java'},
    {'title': 'Algorithms', 'link': 'https://example.com/textbooks/algorithms-book'},
]

ds_youtube_videos = [
    {'title': 'DSA Crash Course', 'link': 'https://www.youtube.com/watch?v=XXXXX'},
    {'title': 'Data Structures in Python', 'link': 'https://www.youtube.com/watch?v=YYYYY'},
]

ds_other_links = [
    {'title': 'GeeksforGeeks - DSA', 'link': 'https://www.geeksforgeeks.org/data-structures/'},
    {'title': 'Codecademy - Learn DSA', 'link': 'https://www.codecademy.com/learn/learn-data-structures-algorithms'},
]
@app.route('/ds')
def ds():
    return render_template('ds.html',ds_papers=ds_papers,
                           ds_practice_questions=ds_practice_questions,
                           ds_textbooks=ds_textbooks,
                           ds_youtube_videos=ds_youtube_videos,
                           ds_other_links=ds_other_links)



@app.route('/interviews-placement')
def interviews_placement():
    return render_template('interviews-placement.html')

@app.route('/data-science')
def data_science():
    return render_template('data-science.html')

@app.route('/gate')
def gate():
    return render_template('gate.html')

@app.route('/programming-languages')
def programming_languages():
    return render_template('programming-languages.html')

@app.route('/web-development')
def web_development():
    return render_template('web-development.html')

@app.route('/focus')
def focus():
    return render_template('focus.html')


if __name__ == '__main__':
    app.run(debug=True)

