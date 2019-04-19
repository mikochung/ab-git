from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, Good, GoodCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class GoodView(ModelView):
    datamodel = SQLAInterface(Good)
    list_columns = ['id', 'title', 'content', 'date', 'goodCat_id']

class GoodCategoryView(ModelView):
    datamodel = SQLAInterface(GoodCategory)
    list_columns = ['id', 'name']


class LocalPageView(BaseView):
    default_view = 'all_deals'

    @expose('/all_deals')
    def all_deals(self):
        param1 = 'All Deals'
        self.update_redirect()
        return self.render_template('local.html', param1 = param1)


class GoodPageView(BaseView):
    default_view = 'auto_and_home_improvement'

    @expose('/auto_and_home_improvement')
    def auto_and_home_improvement(self):
        param1 = 'Auto & Home Improvement'
        self.update_redirect()
        return self.render_template('good.html', param1 = param1)

    @expose('/baby_and_kids/')
    def baby_and_kids(self):
        param1 = 'Baby & Kids'
        self.update_redirect()
        return self.render_template('good.html', param1=param1)


    @expose('/electronics/')
    def electronics(self):
        param1 = 'Electronics'
        self.update_redirect()
        return self.render_template('good.html', param1=param1)

    @expose('/entertainment/')
    def electronics(self):
        param1 = 'Entertainment'
        self.update_redirect()
        return self.render_template('good.html', param1=param1)

    @expose('/for_the_home/')
    def electronics(self):
        param1 = 'For Thr Home'
        self.update_redirect()
        return self.render_template('good.html', param1=param1)

    @expose('/grocery_and_household/')
    def electronics(self):
        param1 = 'Grocery & household'
        self.update_redirect()
        return self.render_template('good.html', param1=param1)

db.create_all()
appbuilder.add_view(LocalPageView, 'All Deals', category="Local")
""" Page View """
appbuilder.add_view(GoodPageView, 'Auto & Home Improvement', category="Good")
appbuilder.add_link("Baby & Kids", href="/GoodPageView/baby_and_kids/", category="Good")
appbuilder.add_link("Electronics", href="/GoodPageView/electronics/", category="Good")
appbuilder.add_link("Entertainment", href="/GoodPageView/entertainment/", category="Good")
appbuilder.add_link("For Thr Home", href="/GoodPageView/for_the_home/", category="Good")
appbuilder.add_link("Grocery & household", href="/GoodPageView/grocery_and_household/", category="Good")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(GoodView, "Good", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(GoodCategoryView, "GoodCategory", icon="fa-folder-open-o", category="Admin")
