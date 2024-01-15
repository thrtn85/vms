def update_related_items(user_profile, field_name, selected_items):
     related_items = getattr(user_profile, field_name).all()

     for item in related_items:
          if item not in selected_items:
               getattr(user_profile, field_name).remove(item)

     for item in selected_items:
          getattr(user_profile, field_name).add(item)
