from Airas_HW_4.file_executor.create import create_file
from Airas_HW_4.file_executor.delete import delete_file
from Airas_HW_4.file_executor.write import write_to_file

print(create_file("adelia", 'txt'))
write_to_file("adelia.txt", "Марлен КРАШ")
print(delete_file("adelia.txt"))