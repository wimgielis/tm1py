from TM1py import TM1pyQueries as TM1, TM1pyLogin, MDXView
import uuid

# establish connection to TM1 Server
login = TM1pyLogin.native('admin', 'apple')

with TM1(ip='', port=8001, login=login, ssl=False) as tm1:
    # random text
    random_string = str(uuid.uuid4())

    # create mdx view
    mdx = "SELECT NON EMPTY {TM1SUBSETALL( [}Clients] )} on ROWS, NON EMPTY {TM1SUBSETALL( [}Groups] )} ON COLUMNS " \
        "FROM [}ClientGroups]"
    mdx_view = MDXView(cube_name='}ClientGroups', view_name='TM1py_' + random_string, MDX=mdx)

    # create mdx view on TM1 Server
    tm1.create_view(view=mdx_view)

    # get view content
    content = tm1.get_view_content(cube_name=mdx_view.cube, view_name=mdx_view.name)

    # print content
    print(content)



