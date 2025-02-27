from typing import Any, Callable

from typing_extensions import Self

from ...binding import BindableProperty, bind, bind_from, bind_to
from ...element import Element


class TextElement(Element):
    text = BindableProperty(on_change=lambda sender, text: sender.on_text_change(text))

    def __init__(self, *, text: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.text = text
        self._text_to_model_text(text)

    def bind_text_to(self,
                     target_object: Any,
                     target_name: str = 'text',
                     forward: Callable = lambda x: x) -> Self:
        """Bind the text of this element to the target object's target_name property.

        The binding works one way only, from this element to the target.

        :param target_object: The object to bind to.
        :param target_name: The name of the property to bind to.
        :param forward: A function to apply to the value before applying it to the target.
        """
        bind_to(self, 'text', target_object, target_name, forward)
        return self

    def bind_text_from(self,
                       target_object: Any,
                       target_name: str = 'text',
                       backward: Callable = lambda x: x) -> Self:
        """Bind the text of this element from the target object's target_name property.

        The binding works one way only, from the target to this element.

        :param target_object: The object to bind from.
        :param target_name: The name of the property to bind from.
        :param backward: A function to apply to the value before applying it to this element.
        """
        bind_from(self, 'text', target_object, target_name, backward)
        return self

    def bind_text(self,
                  target_object: Any,
                  target_name: str = 'text', *,
                  forward: Callable = lambda x: x,
                  backward: Callable = lambda x: x) -> Self:
        """Bind the text of this element to the target object's target_name property.

        The binding works both ways, from this element to the target and from the target to this element.

        :param target_object: The object to bind to.
        :param target_name: The name of the property to bind to.
        :param forward: A function to apply to the value before applying it to the target.
        :param backward: A function to apply to the value before applying it to this element.
        """
        bind(self, 'text', target_object, target_name, forward=forward, backward=backward)
        return self

    def set_text(self, text: str) -> None:
        """Set the text of this element.

        :param text: The new text.
        """
        self.text = text

    def on_text_change(self, text: str) -> None:
        """Called when the text of this element changes.

        :param text: The new text.
        """
        self._text_to_model_text(text)
        self.update()

    def _text_to_model_text(self, text: str) -> None:
        self._text = text
