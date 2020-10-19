def fake_string(string1, replaced_string, new_fake_string, replacement_count):
    result = string1.replace(replaced_string, new_fake_string, replacement_count)
    return result


print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 0))
