# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                                  import Flask
from api.routes.pdf                                         import pdf
# APP ===========================================================================================================================
app                                                         = Flask(__name__)
# BLUEPRINT =====================================================================================================================
app.register_blueprint(pdf)
# INIT ==========================================================================================================================
if __name__ == "__main__": 
    app.run(debug = True)