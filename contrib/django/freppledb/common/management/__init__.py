#
# Copyright (C) 2007-2013 by Johan De Taeye, frePPLe bvba
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.db.models import signals
from django.db import DEFAULT_DB_ALIAS


def createReportPermissions(app, created_models, verbosity, db=DEFAULT_DB_ALIAS, **kwargs):
  # Create the report permissions for the single menu instance we know about.
  if db == DEFAULT_DB_ALIAS:
    appname = app.__name__.replace(".models","")
    from freppledb.menu import menu
    menu.createReportPermissions(appname)
    from freppledb.common.dashboard import Dashboard
    Dashboard.createWidgetPermissions(appname)


signals.post_syncdb.connect(createReportPermissions)
