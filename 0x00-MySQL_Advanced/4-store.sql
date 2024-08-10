-- Decreases quantity of an item after adding a new order
CREATE TRIGGER decrease_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;