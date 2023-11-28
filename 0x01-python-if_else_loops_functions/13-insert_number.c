#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *cursor = *head, *temp = NULL, *temp2 = cursor;

  while (cursor)
  {
    if (cursor->n > number)
    {
      temp = malloc(sizeof(listint_t));
      if (temp == NULL)
        {
          free(temp);
          return (NULL);
        }
      temp->n = number;
      temp->next = temp2->next;
      temp2->next = temp;
      return (temp);
    }
    temp2 = cursor;
    cursor = cursor->next;
  }
  return (NULL);
}