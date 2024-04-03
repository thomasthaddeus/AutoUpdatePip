"""version.py
This module provides the ProjectVersion class, which is used for representing
and manipulating version numbers of a project. The version numbers follow the
semantic versioning scheme, consisting of major, minor, and patch components.

The ProjectVersion class allows for easy manipulation of these components
through methods to increment the major, minor, and patch numbers, and to update
the version string accordingly. It also includes functionality to parse version
strings into ProjectVersion instances and to compare different version
instances for equality.

Example usage:
    version = ProjectVersion(1, 0, 0)
    version.increment_minor()
    print(version)  # Outputs: v1.1.0
"""


class ProjectVersion:
    """
    A class to represent and manipulate project version numbers.

    Attributes:
        version (str): The version number of the project in the format
          'v{major}.{minor}.{patch}'.
    """

    def __init__(self, major: int, minor: int, patch: int) -> None:
        """
        Initializes the ProjectVersion object with major, minor, and patch
        numbers.

        Parameters:
            major (int): The major version number.
            minor (int): The minor version number.
            patch (int): The patch version number.
        """
        self.major = major
        self.minor = minor
        self.patch = patch
        self._update_version()

    def _version_num(self) -> str:
        """
        Retrieves the version number of the project.

        Returns:
            str: The version number as a string.
        """
        return self.version

    def _update_version(self):
        """Updates the version string based on major, minor, and patch numbers."""
        self.version = f'v{self.major}.{self.minor}.{self.patch}'

    def increment_major(self):
        """Increments the major version number and resets the minor and patch numbers."""
        self.major += 1
        self.minor = 0
        self.patch = 0
        self._update_version()

    def increment_minor(self):
        """Increments the minor version number and resets the patch number."""
        self.minor += 1
        self.patch = 0
        self._update_version()

    def increment_patch(self):
        """Increments the patch version number."""
        self.patch += 1
        self._update_version()

    @staticmethod
    def parse_version(version_str: str):
        """
        Parses a version string and returns a ProjectVersion instance.

        Raises:
            ValueError: If the version string is not in the format 'v{major}.{minor}.{patch}'.

        Returns:
            ProjectVersion: The parsed version as a ProjectVersion instance.
        """
        parts = version_str.strip('v').split('.')
        if len(parts) != 3:
            raise ValueError("Version string must be in the format 'v{major}.{minor}.{patch}'")
        major, minor, patch = map(int, parts)
        return ProjectVersion(major, minor, patch)

    def __str__(self):
        """Returns the version string representation."""
        return self.version

    def __eq__(self, other):
        """Checks if two ProjectVersion instances have the same version number."""
        return isinstance(other, ProjectVersion) and self.version == other.version
