from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy()
db.init_app(app)

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

@app.route('/', methods=['POST'])
def index():
    return jsonify({'message': 'Index route'}), 200

@app.route('/issues', methods=['GET', 'POST'])
def issues():
    if request.method == 'GET':
        issues = Issue.query.all()
        if not issues:
            return jsonify({'message': 'No issues found'}), 404
        
        return jsonify({
            'message': 'Issues available',
            'data': [issue.to_dict() for issue in issues]
        }), 200
    
    if request.method == 'POST':
        body = request.get_json()

        if not body:
            return jsonify({'message': 'Invalid request'}), 400
        
        title = body.get('title')
        description = body.get('description')

        if not any([title, description]):
            return jsonify({'message': 'Invalid request'}), 400

        if Issue.query.filter_by(title=title).first():
            return jsonify({'message': 'Issue already exists. Choose a different title.'}), 400
        
        issue = Issue(title=title, description=description)
        db.session.add(issue)
        db.session.commit()

        return jsonify({'message': 'Issue created'}), 201

@app.route('/issues/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def issue(id = None):
    if request.method == 'GET':
        issue = Issue.query.filter_by(id=id).first()
        if not issue:
            return jsonify({'message': 'No issue found'}), 404
        
        return jsonify({
            'message': 'Issue retrieved',
            'data': issue.to_dict()
        }), 200
    
    body = request.get_json()

    if not body:
        return jsonify({'message': 'Invalid request'}), 400
    
    id = body.get('id')
    title = body.get('title')
    description = body.get('description')
    
    issue = Issue.query.filter_by(id=id).first()
    if not issue:
        return jsonify({'message': 'Issue not found'}), 404

    message = None
    if request.method == 'PUT':
        if not any([title, description]):
            return jsonify({'message': 'Invalid request'}), 400
        
        if title: issue.title = title
        if description: issue.description = description
        message = 'Issue updated'
    
    if request.method == 'DELETE':
        db.session.delete(issue)
        message = 'Issue deleted'

    db.session.commit()
    return jsonify({'message': message}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)