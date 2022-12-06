
class NewsLetterAuthor():
    def __init__(self, author_dict:dict) -> None:
        self.__author_dict = author_dict

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}' + 
            f'(display_name={self.display_name}, minecraft_username={self.minecraft_username})'
        )

    @property
    def display_name(self) -> str:
        """Display name of author."""
        return self.__author_dict["display_name"]

    @property
    def name(self) -> str:
        """Like the username of author I guess."""
        return self.__author_dict["name"]
    
    username = name

    @property
    def minecraft_username(self) -> str:
        """Returns the minecraft username of the author."""
        return self.__author_dict["minecraft_username"]

    @property
    def minecraft_uuid(self) -> str:
        """Returns the minecraft uuid of the author."""
        return self.__author_dict["minecraft_uuid"]