from selenium.webdriver.remote.webelement import WebElement


class WebElementUtils:

    @staticmethod
    def get_absolute_xpath(element: WebElement) -> str:
        try:
            return element.parent.execute_script(
                """
                function getPathTo(element) {
                    if (element === document.body)
                        return '//' + element.tagName;

                    let ix = 0;
                    let siblings = element.parentNode.childNodes;

                    for (let i = 0; i < siblings.length; i++) {
                        let sibling = siblings[i];
                        if (sibling === element)
                            return getPathTo(element.parentNode) + '/' + element.tagName + '[' + (ix + 1) + ']';

                        if (sibling.nodeType === 1 && sibling.tagName === element.tagName)
                            ix++;
                    }
                }

                return getPathTo(arguments[0]);
                """,
                element,
            )
        except Exception as e:
            print("Ошибка при получении абсолютного XPath:", str(e))
            return None
