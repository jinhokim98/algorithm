SELECT child_info.ITEM_ID,
       child_info.ITEM_NAME,
       child_info.RARITY
FROM ITEM_TREE child
JOIN ITEM_INFO child_info
  ON child.ITEM_ID = child_info.ITEM_ID
JOIN ITEM_INFO parent_info
  ON child.PARENT_ITEM_ID = parent_info.ITEM_ID
WHERE parent_info.RARITY = 'RARE'
ORDER BY child_info.ITEM_ID DESC;