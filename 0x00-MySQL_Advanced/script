-- Script creating trigger that decrease the quantity
-- of an item on adding a new order.
CREATE TRIGGER after_order_insert AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
