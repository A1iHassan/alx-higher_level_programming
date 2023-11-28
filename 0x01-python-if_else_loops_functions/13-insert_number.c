#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *cursor = *head, *temp = NULL, *temp2 = cursor;

  temp = malloc(sizeof(listint_t));
  if (temp == NULL)
  {
    free(temp);
    return (NULL);
  }
  temp->n = number;
  if (*head == NULL)
  {
    *head = temp;
    temp->next = NULL;
  }
  else
  {
    while (cursor)
    {
      if (cursor->n > number)
      {
        if (cursor == *head)
        {
          *head = temp;
          temp->next = cursor;
          return (temp);
        }
        else
        {
          temp2->next = temp;
          temp->next = cursor;
          return (temp);
        }
      }
      temp2 = cursor;
      cursor = cursor->next;
    }
    temp2->next = temp;
    temp->next = NULL;
    return (temp);
  }
  return (NULL);
}