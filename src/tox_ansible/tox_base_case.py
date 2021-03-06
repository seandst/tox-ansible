class ToxBaseCase(object):
    def __init__(self):
        # Some of the matrix fields we might care about later. They should be
        # copied in the "expand" method below, if you add any more to this
        # area in the future
        self.python = None
        self.ansible = None

    def get_basepython(self):
        """The python version that should be used to execute this, if a
        particular one is requested. If not, then leave it up to the system
        default. The name of the executable is arrived at simply by appending
        the configured python Version to the word "python". So if you have
        specified python as "3.9" then this method will yield "python3.9"

        :return: Python executable to execute against, if any, else None"""
        if self.python is None:
            return None
        return "python" + self.python

    def _expand(self, name):
        """Create a copy of this role, expanded with the additional name field
        and other such niceties.

        :param name: An additional field to be added to the name factors
        :return: A copy of this object with the additional name factor"""
        if hasattr(self, 'role') and hasattr(self, 'scenario'):
            copy = self.__class__(self.role, self.scenario,
                                  [name] + self._name_parts)
        else:
            copy = self.__class__(self._cases, [name] + self._name_parts)
        copy.python = self.python
        copy.ansible = self.ansible
        return copy

    def expand_python(self, version):
        """Create a copy of this Test Case, but add a factor to the name to
        reflect a particular version of Python

        :param version: String representation of Python version (e.g. '2.7')
        :return: A copy of this test case expanded to specify the given version
        of python"""
        copy = self._expand('py' + version.replace('.', ''))
        copy.python = version

        return copy

    def expand_ansible(self, version):
        """Create a copy of this Test CAse, but add a factor to the name to
        reflect a particular version of Ansible

        :param version: String representation of Ansible version (e.g. 2.8)
        :return: A copy of this test case expanded to specify the given version
        of Ansible"""
        copy = self._expand('ansible' + version.replace('.', ''))
        copy.ansible = version

        return copy
