#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
  listint_t *cursor = *head, *temp = *head;
  int i = 0, *j, k = 0;


  while (temp)
  {
    temp = temp->next;
    i++;
  }
  j = malloc(sizeof(int) * i);
  while (cursor)
  {
    j[k] = cursor->n;
    cursor = cursor->next;
    k++;
  }
  for (k = 0; k < i / 2 ; k++)
  {
    if (j[k] != j[i - k])
      {
        free(j);
        return (0);
      }
  }
  free(j);
  return (1);
}