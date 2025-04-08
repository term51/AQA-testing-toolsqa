from typing import Literal

import allure
import pytest

from pages.interactions.draggable_page import DraggablePage
from pages.interactions.droppable_page import DroppablePage
from pages.interactions.resizable_page import ResizablePage
from pages.interactions.selectable_page import SelectablePage
from pages.interactions.sortable_page import SortablePage


@allure.suite('Interactions')
class TestInteractions:
    @allure.feature('Sortable')
    class TestSortable:
        @pytest.mark.parametrize('tab', ['list', 'grid'])
        @allure.title('Sort {tab}')
        def test_sortable(self, driver, tab: Literal['list', 'grid']):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before, after = sortable_page.change_order(tab)
            assert before != after, f"The order of {tab} is not changed"

    @allure.feature('Selectable')
    class TestSelectable:
        @pytest.mark.parametrize('tab', ['list', 'grid'])
        @allure.title('Select {tab}')
        def test_selectable(self, driver, tab: Literal['list', 'grid']):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            items = selectable_page.select_items(tab)
            assert len(items) > 0, f"There are no selected items in {tab}"

    @allure.feature('Resizable')
    class Resizable:
        @allure.title('Check resize of two blocks')
        def test_resizable(driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            size_before = resizable_page.change_box_size_with_restriction(400, 200)
            size_after = resizable_page.change_box_size_with_restriction(-500, -300)
            assert size_before['width'] == 500, "The max width of restriction box must be 500"
            assert size_before['height'] == 300, "The nax height of restriction box must be 300"
            assert size_after['width'] == 150, "The min width must be 150"
            assert size_after['height'] == 150, "The min height must be 150"

            start_x = 150
            start_y = 250
            size_before = resizable_page.change_box_size_without_restriction(start_x, start_y)
            size_after = resizable_page.change_box_size_without_restriction(-350, -450)
            assert size_before['width'] == start_x + 200, f"The width of the box should be increased by {start_x}"
            assert size_before['height'] == start_y + 201, f"The height of the box should be increased by  {start_y}"
            assert size_after['width'] == 20, "The min width of the box must be 20"
            assert size_after['height'] == 20, "The min height of the box must be 20"

    @allure.feature('Droppable')
    class TestDroppable:
        @allure.title('Check simple drag and drop')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            result_text = droppable_page.drop_simple()
            assert result_text == 'Dropped!', "The element was not dropped"

        @allure.title('Check drag and drop for acceptable property of blocks')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_not_acceptable, text_acceptable = droppable_page.drop_accept()
            assert text_not_acceptable == 'Drop here', "The element should not affect the box."
            assert text_acceptable == 'Dropped!', "The element was not dropped."

        @allure.title('Check drag and drop for Prevent Propagation of blocks')
        def test_prevent_propagation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_not_greedy_box, text_not_greedy_box_inner, text_greedy_box, text_greedy_box_inner = \
                droppable_page.drop_prevent_propagation()
            assert text_not_greedy_box == 'Dropped!', "The element has not been changed."
            assert text_not_greedy_box_inner == 'Dropped!', "The element has not been changed."
            assert text_greedy_box == 'Outer droppable', "The element has been changed."
            assert text_greedy_box_inner == 'Dropped!', "The element has not been changed."

        @allure.title('Check drag and drop for revert and not revert blocks')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            before_position, after_position = droppable_page.drop_revert_draggable('will')
            print(f"Will - Before: {before_position}, After: {after_position}")
            assert before_position['x'] != after_position['x'] \
                   and before_position['y'] != after_position['y'], "The element's position should change."

            before_position, after_position = droppable_page.drop_revert_draggable('not_will')
            print(f"Not will - Before: {before_position}, After: {after_position}")
            assert before_position['x'] == after_position['x'] \
                   and before_position['y'] == after_position['y'], "The element's position should not change."

    @allure.feature('Draggable')
    class TestDraggable:
        @allure.title('Check simple dragging')
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before_position, after_position = draggable_page.simple_drag_box()
            assert before_position != after_position, "The element's position should change."

        @allure.title('Check drag only on X and only on Y axes')
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before_only_x_position, before_only_y_position, after_only_x_position, after_only_y_position = \
                draggable_page.axis_restricted_draggable()

            assert before_only_x_position['x'] != after_only_x_position['x'] \
                   and before_only_x_position['y'] == after_only_x_position['y'], \
                "The only element's x position should change."

            assert before_only_y_position['x'] == after_only_y_position['x'] \
                   and before_only_y_position['y'] != after_only_y_position['y'], \
                "The only element's y position should change."
