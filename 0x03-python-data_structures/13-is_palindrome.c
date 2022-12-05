#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 1 if list is palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *list_arr;
	int num;

	num = 0;
	curr = head;
	while (curr)
	{
		num++;
		curr = curr->next;
	}
	if (!head)
		return (1);


