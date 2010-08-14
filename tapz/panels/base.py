from tapz.panels.options import PanelOptions
from tapz.site import site

class PanelMeta(type):
    """
    Metaclass for all Panels
    """
    def __new__(cls, name, bases, attrs):
        super_new = super(PanelMeta, cls).__new__
        parents = [b for b in bases if isinstance(b, PanelMeta)]
        if not parents:
            # If this isn't a subclass of Panel, don't do anything special.
            return super_new(cls, name, bases, attrs)

        new_class = super_new(cls, name, bases, {})
        meta = attrs.pop('Meta', None)
        new_class.add_to_class('_meta', PanelOptions(meta))
        for attr_name, attr_value in attrs.items():
            new_class.add_to_class(attr_name, attr_value)
        site.register(new_class)
        return new_class

    def add_to_class(cls, name, value):
        """
        Add the value to the class object either by calling
        contribute_to_class or setting it directly
        """
        if hasattr(value, 'contribute_to_class'):
            value.contribute_to_class(cls, name)
        else:
            setattr(cls, name, value)

class Panel(object):
    __metaclass__ = PanelMeta

    def add_event(self, data):
        """
        Another event named `name` just occured (`data` contains all the
        information for that event), process and store it.
        """
        cleaned_data = self.clean(data)
        # slice dimensions
        dimensions = {}
        for dim in self.get_dimensions():
            # panels can define custom ways to sli
            dimension_method = 'dimension_%s' % dim
            if hasattr(self, dimension_method):
                dimensions[dim] = getattr(self, dimension_method)(cleaned_data[dim])
            else:
                dimensions[dim] = [cleaned_data[dim]]
        CALL_HONZA_CODE(dimensions, cleaned_data)

    def clean(self, data):
        """
        Clean the data input data. If a method exists named ``clean_<field-name>``
        then call it
        """
        cleaned_data = {}
        for key, value in data.iteritems():
            clean_method = 'clean_%s' % key
            if hasattr(self, clean_method):
                cleaned_data[key] = getattr(self, clean_method)(value)
            else:
                cleaned_data[key] = value
        return cleaned_data

    def get_data(self, dimensions, limit=None):
        """
        Return all the data for this panel, if `limit` is given, only limit to
        last `limit` records.
        """
        pass

    def get_default_renderer(self):
        """
        Get default rendering class for this type of panel.
        """
        pass

    def render(self, limit=None, renderer=None):
        """
        Retrive and render data for this panel.
        """
        renderer = renderer or self.get_default_renderer()
        return renderer.render(self.get_data(limit=limit))