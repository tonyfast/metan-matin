"""UI routes"""

from metaregistry import app
import os
# from metaregistry import gh

@app.route('/')
@app.route('/<user>/<repo>')
def index(user = 'tonyfast',
          repo = 'Organic-Field-Effect-Transistor'):


    from github import Github
    from metaregistry import app
    import yaml
    from pandas import pd


    gh = Github(app.config['GH_USER'], app.config['GH_KEY'])


    repo = gh.get_user(user).get_repo(repo)

    # Initialize Unique Keys
    allkeys = list()

    # Contents of datapages folder on gh-pages branch
    fil = repo.get_dir_contents(path="_data", ref="gh-pages")

    # 1. Loop over the contents of data file
    # 2. Import YAML
    # 3. Find unique fields interatively
    for ii, n in enumerate(fil):
        mdcontent = pd.DataFrame( yaml.load( n.decoded_content ) )
        keys = mdcontent.columns.tolist();
        allkeys = list( set( allkeys).union( list(keys) ))
        if ii > 3:
          break
        # file number, number of unique metadata fields

    return str(allkeys)


@app.route('/bikes/<int:id>')
def bikes(id):
    return 'Bike {0}'.format(id)
