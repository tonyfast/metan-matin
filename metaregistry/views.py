"""UI routes"""

from metaregistry import app
import os
# from metaregistry import gh


@app.route('/')
def index():

  """
    from github import Github
    import yaml
    user = 'tonyfast'
    repo_name = 'Organic-Field-Effect-Transistor'
    repo = gh.get_user(user).get_repo(repo_name)

    # Initialize Unique Keys
    allkeys = list()

    # Contents of datapages folder on gh-pages branch
    fil = repo.get_dir_contents(path="_data", ref="gh-pages")

    # 1. Loop over the contents of data file
    # 2. Import YAML
    # 3. Find unique fields interatively
    for ii, n in enumerate(fil):
        mdcontent = yaml.load( n.decoded_content )
        keys = [ x for x in mdcontent]
        allkeys = list( set( allkeys).union( list(keys) ))
        if ii > 3:
          break
        # file number, number of unique metadata fields

    return str(allkeys)
  """
  
  return app.config['GH_USER']


@app.route('/bikes/<int:id>')
def bikes(id):
    return 'Bike {0}'.format(id)
