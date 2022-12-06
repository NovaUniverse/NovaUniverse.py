
class NewsLetterType():
    def __init__(self, type_dict:dict) -> None:
        self.__type_dict = type_dict

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}' + 
            f'(title={self.title}, css_class={self.css_class})'
        )

    @property
    def title(self) -> str:
        return self.__type_dict["title"]

    @property
    def css_class(self) -> str:
        return self.__type_dict["css_class"]