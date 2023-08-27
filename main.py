def main():


    males = (int(input('Number of males in the class: ')))
    females = (int(input('Number of females in the class: ')))

    total_students = (males + females)
    m_perc = (males / total_students * 100)
    f_perc = (females / total_students * 100)

    


    print(f'The total number of students: {total_students}')
    print(f'The number of males and females: {males, females}')
    print(f'The percentage of males and females: {m_perc:.2f} {f_perc:.2f}')
 
 
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
