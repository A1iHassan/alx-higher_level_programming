#include "lists.h"

int check_cycle(listint_t *list)
{
  listint_t *current = list;

  while (current)
  {
    if (current <= current->next)
      return (1);
    current = current->next;
  }
  return (0);
}
